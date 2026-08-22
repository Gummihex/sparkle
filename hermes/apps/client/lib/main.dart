import 'package:flutter/material.dart';

void main() => runApp(const HermesApp());

class HermesApp extends StatelessWidget {
  const HermesApp({super.key});
  @override
  Widget build(BuildContext context) => MaterialApp(
    title: 'HERMES LIGHT HUB',
    debugShowCheckedModeBanner: false,
    theme: ThemeData(brightness: Brightness.dark, colorSchemeSeed: Colors.cyan, useMaterial3: true),
    home: const Dashboard(),
  );
}

class Dashboard extends StatelessWidget {
  const Dashboard({super.key});
  @override
  Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(title: const Text('HERMES LIGHT HUB'), actions: [
      IconButton(onPressed: () {}, icon: const Icon(Icons.radar)),
      IconButton(onPressed: () {}, icon: const Icon(Icons.settings)),
    ]),
    body: GridView.extent(maxCrossAxisExtent: 330, padding: const EdgeInsets.all(20), mainAxisSpacing: 16, crossAxisSpacing: 16,
      children: const [
        HubCard('GERÄTE', 'Hue · Nanoleaf · Govee · Twinkly', Icons.hub),
        HubCard('DISCOVERY', 'WLAN · LAN · Bluetooth · Matter', Icons.radar),
        HubCard('RÄUME', 'Wohnzimmer · Gaming · Schlafzimmer', Icons.meeting_room),
        HubCard('SZENEN', 'Movie · Gaming · Party · Relax', Icons.auto_awesome),
        HubCard('SCREEN SYNC', 'Windows Desktop Capture bereit', Icons.monitor),
        HubCard('MUSIC SYNC', 'Audio-Reaktiv Engine bereit', Icons.music_note),
        HubCard('AI', 'Szenen + Sprache + Automation', Icons.psychology),
        HubCard('STATS', 'Latenz · Geräte · Netzwerk', Icons.insights),
      ],
    ),
  );
}

class HubCard extends StatelessWidget {
  final String title, subtitle; final IconData icon;
  const HubCard(this.title, this.subtitle, this.icon, {super.key});
  @override
  Widget build(BuildContext context) => Card(child: Padding(padding: const EdgeInsets.all(20), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
    Icon(icon, size: 34), const Spacer(), Text(title, style: Theme.of(context).textTheme.labelLarge), const SizedBox(height: 8), Text(subtitle, style: Theme.of(context).textTheme.bodyMedium)
  ])));
}
