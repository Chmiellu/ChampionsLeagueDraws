# ChampionsLeagueDraws
This application is designed to facilitate the drawing of playoff pairs for the Champions League. It utilizes the FastAPI framework to expose two endpoints:

How it Works
The application leverages the generate_pairs function from the draw_service module to randomly pair teams for the playoff stage. The draw results can be accessed in both JSON and HTML formats, making it convenient for different use cases.

Endpoints
1. /drawpairsJSON: Returns a list of tuples representing the playoff pairs in JSON format.

2. /results: Presents the draw results in an HTML response. The pairs are displayed in a visually appealing format, making it easy to read and share.

Feel free to explore and integrate this application into your workflow for Champions League draws!

## DrawProcedure
- Two seeding pots will be formed: one consisting of group winners and the other of runners-up.
- No team can play a club from their group or any side from their own association.
- Seeded group winners will be away in the round of 16 first legs and at home in the return matches.
