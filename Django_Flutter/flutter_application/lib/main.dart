import 'package:flutter/material.dart';
import 'package:flutter_application/providers/task_provider.dart';
import 'package:flutter_application/screens/home.dart';
import 'package:provider/provider.dart';

void main() {
  runApp(const PlanApp());
}

class PlanApp extends StatelessWidget {
  const PlanApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => PlanProvider(),
      child: const MaterialApp(
        title: '일정관리',
        home: HomeScreen(),
      ),
    );
  }
}
