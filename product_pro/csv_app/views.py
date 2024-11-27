from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import json

def csv_upload_view(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']

        try:
            # Read the uploaded CSV file into a DataFrame
            df = pd.read_csv(csv_file)
            # Save the DataFrame data and columns to the session
            request.session['csv_data'] = df.to_json(orient='records')
            request.session['csv_columns'] = list(df.columns)  # Store column names

            if 'csv_data' in request.session and 'csv_columns' in request.session:
                print("CSV data and columns saved to session successfully.")
        except Exception as e:
            return render(request, 'csv_upload.html', {'error': f"Error processing CSV file: {str(e)}"})

    return render(request, 'csv_upload.html')


def fetch_csv_data(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    # Get the CSV data and columns from the session
        csv_data = request.session.get('csv_data', None)
        csv_columns = request.session.get('csv_columns', None)

        if not csv_data or not csv_columns:
            return JsonResponse({'error': 'No CSV data available. Please upload a file first.'}, status=400)

        # Convert JSON data back to a DataFrame
        df = pd.DataFrame(json.loads(csv_data))

        # Pagination parameters from DataTables
        draw = int(request.GET.get('draw', 1))
        start = int(request.GET.get('start', 0))
        length = int(request.GET.get('length', 10))
        # search_value = request.GET.get('search[value]', '')

        # # Filter the DataFrame based on search
        # if search_value:
        #     df = df[df.apply(lambda row: row.astype(str).str.contains(search_value, case=False).any(), axis=1)]

        # Sorting (if specified)
        order_column = request.GET.get('order[0][column]', None)
        order_dir = request.GET.get('order[0][dir]', 'asc')

        if order_column:
            order_column = csv_columns[int(order_column)]
            ascending = order_dir == 'asc'
            df = df.sort_values(by=order_column, ascending=ascending)

        # Total records before and after filtering
        records_total = len(json.loads(csv_data))
        records_filtered = len(df)

        # Paginate the data
        df_page = df.iloc[start:start + length]

        # Convert DataFrame to list of records for DataTables
        data = df_page.to_dict(orient='records')

        # Return JSON response for DataTables
        return JsonResponse({
            'draw': draw,
            'recordsTotal': records_total,
            'recordsFiltered': records_filtered,
            'data': data
        })

    return render(request, 'csv_table.html')