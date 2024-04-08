import 'dart:collection';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter_application/models/plan.dart';
import 'package:http/http.dart' as http;

class PlanProvider extends ChangeNotifier {
  PlanProvider() {
    fetchSolutions();
  }
  List<Solution> _solutions = [];
  UnmodifiableListView<Solution> get allSolutions =>
      UnmodifiableListView(_solutions);

  fetchSolutions() async {
    var url = Uri.parse('http://localhost:8000/solution');
    // var url = Uri.parse('http://172.16.104.99:8000/solution');
    final response = await http.get(url);
    if (response.statusCode == 200) {
      print("response 200");
      var data = jsonDecode(utf8.decode(response.bodyBytes)) as List;
      _solutions =
          data.map<Solution>((json) => Solution.formJason(json)).toList();
      notifyListeners(); // 변경사항 알림
    } else {
      print("response failed");
    }
  }
}
