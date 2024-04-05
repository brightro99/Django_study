import 'package:flutter/material.dart';
import 'package:flutter_application/models/plan.dart';

class SolutionListItem extends StatelessWidget {
  const SolutionListItem({super.key, required this.solution});
  final Solution solution;

  @override
  Widget build(BuildContext context) {
    var tile = ListTile(
      title: Text(solution.solution),
    );
    return tile;
  }
}
