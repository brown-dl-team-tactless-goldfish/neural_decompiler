class Solution {
private:
    vector<string> split(string str) {
        vector<string> words;
        string word = "";
        
        for(char c : str) {
            if(c == ' ') {
                words.push_back(word);
                word = "";
            } 
            else {
                word += c;
            }
        }
        
        words.push_back(word);
        return words;
    }

    string join(vector<string> words) {
        string str = "";
        for(int i = 0; i < words.size(); i++) {
            str += words[i];
            if(i < words.size() - 1) {
                str += " ";
            }
        }
        return str;
    }
public:
    string capitalizeTitle(string title) {
        // If the string is empty, return an empty string
        if(title.empty()) {
            return "";
        }

        // Split the string into words
        vector<string> words = split(title);

        // Capitalize each word
        for(int i = 0; i < words.size(); i++) {
            string word = words[i];

            if (word.length() <= 2) {
                // Change all letters to lowercase
                transform(word.begin(), word.end(), word.begin(), ::tolower);
            } 
            else {
                // Change first letter to uppercase and remaining letters to lowercase
                word[0] = toupper(word[0]);
                transform(word.begin() + 1, word.end(), word.begin() + 1, ::tolower);
            }

            words[i] = word;
        }

        // Join the words back into a single string
        string capitalizedTitle = join(words);
        return capitalizedTitle;
    }
};