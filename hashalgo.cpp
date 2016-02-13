//converting timestamp to hashkey

#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
 
// Function to generate a short url from intger ID
string idToShortURL(long long n)
{
    // Map to store 62 possible characters
    char map[] = "ABCDEF0123456789";
 
    string shorturl;
 
    // Convert given integer id to a base 62 number
    while (n)
    {
        // use above map to store actual character
        // in short url
        shorturl.push_back(map[n%16]);
        n = n/16;
    }
 
    // Reverse shortURL to complete base conversion
    reverse(shorturl.begin(), shorturl.end());
 
    return shorturl;
}
 
// Function to get integer ID back from a short url
long long shortURLtoID(string shortURL)
{
    long long id = 0; // initialize result
 
    // A simple base conversion logic
    for (int i=0; i < shortURL.length(); i++)
    {
        if ('A' <= shortURL[i] && shortURL[i] <= 'F')
          id = id*16 + shortURL[i] - 'A';
        if ('0' <= shortURL[i] && shortURL[i] <= '9')
          id = id*16 + shortURL[i] - '0' +  6;
    }
    return id;
}
 
// Driver program to test above function
int main()
{
    long long n = 130155120116;
    string shorturl = idToShortURL(n);
    cout << "Generated short url is " << shorturl << endl;
    cout << "Id from url is " << shortURLtoID(shorturl);
    return 0;
}
