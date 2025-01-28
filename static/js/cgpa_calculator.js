function calculateCGPA() {
    var totalCredits = 0;
    var totalGradePoints = 0;
    var grades = document.querySelectorAll('.grade');
    var credits = document.querySelectorAll('.credit');

    for (var i = 0; i < grades.length; i++) {
        var grade = grades[i].value;
        var credit = parseFloat(credits[i].value);
        var gradePoint = getGradePoint(grade);
        totalCredits += credit;
        totalGradePoints += (gradePoint * credit);
    }

    var cgpa = totalGradePoints / totalCredits;
    document.getElementById('cgpa-result').innerText = "Your CGPA is: " + cgpa.toFixed(2);
}

function getGradePoint(grade) {
    switch (grade) {
        case "A": return 4.0;
        case "B": return 3.0;
        case "C": return 2.0;
        case "D": return 1.0;
        case "F": return 0.0;
        default: return 0;
    }
}
