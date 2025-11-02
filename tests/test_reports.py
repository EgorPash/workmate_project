from src.reports import AverageRatingReport


def test_average_rating_report_generate():
    data = {'apple': [4.5, 4.6], 'samsung': [4.8], 'xiaomi': [4.3, 4.4]}
    report = AverageRatingReport()
    result = report.generate(data)

    assert len(result) == 3
    assert result[0]['brand'] == 'samsung'
    assert result[0]['rating'] == 4.8
    assert result[1]['brand'] == 'apple'
    assert result[1]['rating'] == 4.55


def test_average_rating_report_empty():
    report = AverageRatingReport()
    result = report.generate({})
    assert result == []
