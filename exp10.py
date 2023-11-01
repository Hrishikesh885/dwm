#Get web page and link data as suer input
web_pages=input("Enter web pages (comma seperated): ").split(",")
links={}
for page in web_pages:
    linked_pages=input(f"Enter pages linked from {page} (comma sepreated, press enter for none)").split(",")
    links[page]=linked_pages

#initialize the page rank values for each web page
init_rank=round(1/len(web_pages),3)
pagerank={page:init_rank for page in web_pages}

#define the damping factor
damping_factor=float(input("Enter the damping factor: "))

#number of iterations
iterations = int(input("Enter the number of iterations"))

#perform page rank calclulations
for i in range(iterations):
    for page in web_pages:
        new_rank=(1-damping_factor)
        for linking_page,linked_pages in links.items():
            if page in linked_pages:
                num_links=len(linked_pages)
                new_rank+=damping_factor*(pagerank[linking_page]/num_links)
            pagerank[page]=new_rank
    
    print(f"iteration{i+1}\n")
    for page,rank in pagerank.items():
        print(f"Page {page}: PageRank {rank:4f}")