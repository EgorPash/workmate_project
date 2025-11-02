from src.main import main
import sys

def test_main_integration(capsys, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['main.py', '--files', 'data/products1.csv', '--report', 'average-rating'])
    main()
    captured = capsys.readouterr()
    assert 'apple' in captured.out
