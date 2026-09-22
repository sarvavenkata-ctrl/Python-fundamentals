import importlib.util
from pathlib import Path

import pytest

module_path = Path(__file__).resolve().parents[1] / "marks_grade_predictor.py"
spec = importlib.util.spec_from_file_location("marks_grade_predictor", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_get_grade_thresholds():
    assert module.get_grade(90) == "A+"
    assert module.get_grade(89) == "A"
    assert module.get_grade(69) == "C"
    assert module.get_grade(59) == "D"


def test_calculate_summary_returns_expected_metrics():
    summary = module.calculate_summary([85, 90, 78, 88, 92])

    assert summary["average_mark"] == pytest.approx(86.6)
    assert summary["grade"] == "A"
    assert summary["performance"] == "Distinction"


def test_plot_marks_writes_requested_output(tmp_path):
    output_path = tmp_path / "custom_chart.png"

    module.plot_marks(["Math", "Science", "English"], [80, 90, 70], output_path=output_path)

    assert output_path.exists()
    assert output_path.stat().st_size > 0
