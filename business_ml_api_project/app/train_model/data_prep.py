import pandas as pd
import numpy as np

class DataPipeline:
    """Подготовка данных"""
    
    def __init__(self):
        """Параметры класса"""
        self.median = None
                
    def fit(self, df):
        """Сохранение статистик"""
        
        # Расчет медиан
        self.medians = df.median()
               
    def transform(self, df):
        """Трансформация данных"""
        
        # 1. Убираем ненужные признаки.

        df = df.drop(['Unnamed: 0','id', 'Gender', 'Flight Distance', 'Departure/Arrival time convenient',
                    'Ease of Online booking', 'Food and drink', 'Inflight entertainment',
                    'On-board service', 'Leg room service', 'Departure Delay in Minutes', 'Arrival Delay in Minutes'], axis=1)

        # 2. Кодирование категориальных признаков
        
        df['Gender'].replace(('Male', 'Female'), (1, 0), inplace=True)
        df['Customer Type'].replace(('Loyal Customer', 'disloyal Customer'), (1, 0), inplace=True)
        df['Type of Travel'].replace(('Business travel', 'Personal Travel'), (1, 0), inplace=True)
        df['Class'].replace(('Business', 'Eco', 'Eco Plus'), (2, 0, 1), inplace=True)
        df['satisfaction'].replace(('neutral or dissatisfied', 'satisfied'), (0, 1), inplace=True)
        
        df.fillna(self.medians, inplace=True)      
        return df