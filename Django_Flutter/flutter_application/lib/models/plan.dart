class Solution {
  int id;
  String solution;

  Solution({required this.id, required this.solution});

  factory Solution.formJason(Map<String, dynamic> json) {
    return Solution(
      id: json['id'],
      solution: json['solution'],
    );
  }

  dynamic toJson() => {
        'solution': solution,
      };
}
