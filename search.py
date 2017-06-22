import webbrowser
import sys
try:
    from google import search
except ImportError:
    print("No module named 'google' found, try 'pip install google' ")
ser_res=""
while(ser_res!='N'):
    sys.stdout.write("\n| Google Search | >>  ")
    query=raw_input()
    print(":::::::::::::TOP RESULTS:::::::::::::::")
    weblist=[]
    i=1
    for j in search(query, tld="co.in", num=10, stop=1, pause=2):
        weblist.append(j)
        print("\n"+str(i)+" > "+weblist[i-1])
        i=i+1
    view_res=""
    while(view_res!='N'):
        sys.stdout.write("\n| Enter Webpage to view (multiple using ',') | >>  ")
        page_res=input()
        if(type(page_res)!=tuple):
            webbrowser.open_new_tab(weblist[page_res-1])
        else:
            for x in page_res:
                webbrowser.open(weblist[x-1])
        sys.stdout.write("\n| View more pages ?(Y|N) | >>")
        view_res=raw_input()
    sys.stdout.write("\n| Search Again ?(Y|N) | >>")
    ser_res=raw_input()
print(":::::::::::::THANK YOU:::::::::::::::")
sys.exit()