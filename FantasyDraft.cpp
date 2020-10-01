using namespace std;
#include <iostream>
#include <unordered_set>

class Owner {
  public:
    int Q;
    string * preferences;
    string * roster;
    int index = 0;
};

int main() {

    int N, K, P;
    cin >> N >> K;

    Owner teams[N];

    for (int i = 0; i < N; i++) {
        cin >> teams[i].Q;

        teams[i].preferences = new string[teams[i].Q];
        teams[i].roster = new string[K];

        for (int j = 0; j < teams[i].Q; j++) {
            cin >> teams[i].preferences[j];
        }
        // for (int j = 0; j < teams[i].Q; j++) {
        //     cout << teams[i].preferences[j] << " ";
        // }
        // cout << "\n";
    };

    cin >> P;

    string players[P];

    for (int i = 0; i < P; i++) {
        cin >> players[i];
    }

    int playersIndex = 0;

    unordered_set<string> taken;

    for (int k = 0; k < K; k++) {
        // k is the round of the draft
        //cout << "Round " << k << "\n";
        for (int n = 0; n < N; n++) {
            //cout << "Team " << n << "\n";
            // teams[n] is the current team
            if (teams[n].index < teams[n].Q) {
                while ( taken.find( teams[n].preferences[teams[n].index] ) != taken.end()
                && teams[n].index < teams[n].Q ) {
                    teams[n].index++;
                    if (teams[n].index >= teams[n].Q) break;
                }
            }
            //cout << "Passed while\n";
            if (teams[n].index < teams[n].Q) {
                //cout << "If\n";
                // not all preferences have been exhausted
                teams[n].roster[k] = teams[n].preferences[teams[n].index];
                taken.insert(teams[n].roster[k]);
                teams[n].index++;
            } else { //if (teams[i].index >= teams[i].Q) {
                // takes from players list indescriminately
                // preferences list has been exhausted
                //cout << "Else\n";
                while ( taken.find( players[playersIndex] ) != taken.end()
                && playersIndex < P ) {
                    playersIndex++;
                    if (playersIndex >= P) break;
                }

                teams[n].roster[k] = players[playersIndex];
                taken.insert(teams[n].roster[k]);
                playersIndex++;
            }
            //cout << teams[n].roster[k] << " " << playersIndex << "\n";
        }
    }

    for (int n = 0; n < N; n++) {
        // cout << teams[n].roster << " " << teams[n].preferences << " ";
        for (int k = 0; k < K; k++) {
            if (k != 0) {
                cout << " ";
            }
            cout << teams[n].roster[k];
        }
        cout << "\n";
    }

    return 0;
}