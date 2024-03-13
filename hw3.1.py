from datetime import datetime

def get_days_from_today(date):
    try:  
        input_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        date_difference = current_date - input_date
        
        return date_difference.days 
    
    except ValueError:
        
        return print ("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'.")

input_date = input (f"Введіть дату в форматі рррр-мм-дд:  ")
result = get_days_from_today (input_date)
if result is not None:
    print (f"Між {input_date} та поточною датою: {result}")
