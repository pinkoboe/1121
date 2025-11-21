# 파일 경로: my_math_package/stats/averages.py

def calculate_mean(numbers):
    """
    숫자 리스트를 받아 평균을 계산합니다.
    리스트가 비어있으면 ValueError를 발생시킵니다.
    """
    if not numbers:
        raise ValueError("평균을 계산할 데이터가 없습니다. 리스트가 비어있습니다.")
    
    return sum(numbers) / len(numbers)