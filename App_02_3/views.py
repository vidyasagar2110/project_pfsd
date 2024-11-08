from django.shortcuts import render 
 
def home(request): 
    context = { 
        'name': 'T. Vidya Sagar', 
        'contact': '7901480808', 
        'email': '2310080002@klh.edu.in', 
        'education': 'B.Tech (AI&DS)', 
        'experience': 'Fresher', 
        'skills': [ 
            'Programming Languages: Python, Java, C', 
            'Version Control: Git, GitHub', 
            'Cloud Computing: AWS' 
        ], 
        'projects': [ 
            {'name': 'Fashion_matcher', 'description': 'A Django project for matching clothing based on URLs.'}, 
            {'name': 'Automatic Operation of Railway Gates', 'description': 'Automates the process of operating railway gates.'} 
        ], 
        'certifications': ['AWS Certified Solutions Architect', 'Python for Data Science'], 
        'achievements': ['Won Hackathon 2023', 'Top 10 in AI challenge'], 
        'hobbies': ['Reading', 'Gaming', 'Coding'], 
        'social_links': { 
            'LinkedIn': 'https://linkedin.com/in/yourprofile', 
            'GitHub': 'https://github.com/vidyasagar2110', 
            'Twitter': 'https://twitter.com/yourhandle' 
        }, 
        'address': 'Uppal, Hyderabad - 500039'  # Add your actual address here 
    } 
    return render(request, 'App_02_3/home.html', context)