import 'package:flutter/material.dart';
import 'package:flutter_application/providers/task_provider.dart';
import 'package:flutter_application/widgets/solution_list.dart';
import 'package:provider/provider.dart';

class SolutionTab extends StatelessWidget {
  const SolutionTab({super.key});

  @override
  Widget build(BuildContext context) {
    var consumer = Consumer<PlanProvider>(
      builder: (context, value, child) =>
          SolutionList(solutions: value.allSolutions),
    );
    return consumer;
  }
}
