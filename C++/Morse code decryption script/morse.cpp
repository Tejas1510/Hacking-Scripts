#include <bits/stdc++.h>
#define fio ios_base::sync_with_stdio(false); cin.tie(NULL);
#define mp make_pair
#define endl "\n"
#define forn(x, n) for (int i = x; i < n; i++)

using namespace std;
//Sauparna Gupta

int main()
{
    freopen("INPUT.txt","r",stdin);
    freopen("OUTPUT.txt","w",stdout);
    string s,s1="",s2="";
    getline(cin,s);
    s+=" ";int n=s.length();
    map<string,char> m;
    m.insert(mp(".-",'a'));
    m.insert(mp("-...",'b'));
    m.insert(mp("-.-.",'c'));
    m.insert(mp("-..",'d'));
    m.insert(mp(".",'e'));
    m.insert(mp("..-.",'f'));
    m.insert(mp("--.",'g'));
    m.insert(mp("....",'h'));
    m.insert(mp("..",'i'));
    m.insert(mp(".---",'j'));
    m.insert(mp("-.-",'k'));
    m.insert(mp(".-..",'l'));
    m.insert(mp("--",'m'));
    m.insert(mp("-.",'n'));
    m.insert(mp("---",'o'));
    m.insert(mp(".--.",'p'));
    m.insert(mp("--.-",'q'));
    m.insert(mp(".-.",'r'));
    m.insert(mp("...",'s'));
    m.insert(mp("-",'t'));
    m.insert(mp("..-",'u'));
    m.insert(mp("...-",'v'));
    m.insert(mp(".--",'w'));
    m.insert(mp("-..-",'x'));
    m.insert(mp("-.--",'y'));
    m.insert(mp("--..",'z'));
    m.insert(mp(".----",'1'));
    m.insert(mp("..---",'2'));
    m.insert(mp("...--",'3'));
    m.insert(mp("....-",'4'));
    m.insert(mp(".....",'5'));
    m.insert(mp("-....",'6'));
    m.insert(mp("--...",'7'));
    m.insert(mp("---..",'8'));
    m.insert(mp("----.",'9'));
    m.insert(mp("-----",'0'));
    m.insert(mp("·-·-·-",'.'));
    m.insert(mp("--··--",','));
    m.insert(mp("-·-·-·",';'));
    m.insert(mp("··--··",'?'));
    m.insert(mp("---···",':'));
    m.insert(mp("·----·",'\''));
    m.insert(mp("·-··-·",'\"'));
    m.insert(mp("-·--·-",')'));
    m.insert(mp("-·--·",'('));
    forn(0,n)
    {
        if(s[i]==' '&&s[i-1]==' ')
        {
            s1+=' ';
            i+=3;
        }
        else if(s[i]==' '&&s[i-1]!=' ')
        {
            s1+=m[s2];
            s2="";
        }
        else
        {
            s2+=s[i];
        }
    }
    cout<<s1<<endl;
}