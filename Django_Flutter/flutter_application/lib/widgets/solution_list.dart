import 'package:flutter/material.dart';
import 'package:flutter_application/models/plan.dart';
import 'package:flutter_application/widgets/solution_list_item.dart';

class SolutionList extends StatelessWidget {
  const SolutionList({super.key, required this.solutions});
  final List<Solution> solutions;

  @override
  Widget build(BuildContext context) {
    return ListView(
      children: getChildrenSolution(),
    );
  }

  List<Widget> getChildrenSolution() {
    var list = solutions
        .map((solution) => SolutionListItem(solution: solution))
        .toList();
    return list;
  }
}
