import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:flutter_application/tabs/solution.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen>
    with SingleTickerProviderStateMixin {
  late TabController controller;
  @override
  void initState() {
    super.initState();
    controller = TabController(length: 1, vsync: this);
  }

  @override
  Widget build(BuildContext context) {
    if (kIsWeb) {
      // 웹용 UI
      return Scaffold(
        appBar: AppBar(
          title: Row(
            children: [
              const Expanded(child: Center(child: Text('Todo List (Web)'))),
              IconButton(
                icon: const Icon(Icons.add),
                onPressed: () {
                  print("press add");
                },
                padding: const EdgeInsets.only(right: 50.0),
              )
            ],
          ),
          bottom: TabBar(
            controller: controller,
            tabs: const [
              Tab(
                icon: Icon(Icons.audiotrack),
                text: "솔루션",
              )
            ],
          ),
        ),
        body: TabBarView(
          controller: controller,
          children: const [
            Center(child: SolutionTab())
            // child: Text("???"))
          ],
        ),
      );
    } else {
      return Scaffold(
        appBar: AppBar(
          title: const Text('Todo List'),
          actions: [
            IconButton(
              icon: const Icon(Icons.add),
              onPressed: () {
                print("press add");
              },
            )
          ],
          bottom: TabBar(
            controller: controller,
            tabs: const [
              Tab(
                icon: Icon(Icons.audiotrack),
                text: "솔루션",
              )
            ],
          ),
        ),
        body: TabBarView(
          controller: controller,
          children: const [SolutionTab()],
        ),
      );
    }
  }
}
