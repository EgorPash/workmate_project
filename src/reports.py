from typing import Dict, List, Any
from statistics import mean


class Report:

    def generate(self, data: Dict[str, List[float]]) -> List[Dict[str, Any]]:
        raise NotImplementedError


class AverageRatingReport(Report):

    def generate(self, data: Dict[str, List[float]]) -> List[Dict[str, Any]]:
        averages = []
        for brand, ratings in data.items():
            if ratings:  # Только если есть рейтинги
                avg = round(mean(ratings), 2)
                averages.append({'index': None, 'brand': brand, 'rating': avg})

        averages.sort(key=lambda x: (-x['rating'], x['brand']))

        for i, item in enumerate(averages, start=1):
            item['index'] = i

        return averages
