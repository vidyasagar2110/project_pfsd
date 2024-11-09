from django.shortcuts import render

def personal_profile(request):
    context = {
        'name': 'T. Vidya Sagar',
        'contact': '7901480808',
        'email': '2310080002@klh.edu.in',
        'address': 'Hyderabad, India',
        'education': [
            'B.tech(Ai&ds), KLH'
            'Intermediate, Sri Chaitanya - 98%',
            'Schooling, NRI Indian Springs - 99%'
        ],
        'experience': 'Fresher',  
        'skills': ['Python', 'Java', 'C', 'GitHub', 'AWS'],
        'projects': [
            {'name': 'Automatic Operation of Railway Gates', 
             'description': 'An automated system for railway crossing gates using sensors to enhance safety.'},
            {'name': 'Fashion Matcher', 
             'description': 'A Django-based app matching clothing items from URLs, with gender-specific navigation for a personalized shopping experience.'}
        ],
        'certifications': ['AWS CLOUD PRACTIONER', 'MongoDB'],  # Add your certifications here
        'achievements': ['won in hackerthon 2023', 'Top 10 in AI Challenge'],  # Add your achievements here
        'hobbies': ['Reading', 'Coding', 'Traveling'],  # Add your hobbies here
        'social_links': {
            'LinkedIn': 'https://www.linkedin.com/in/yourprofile',
            'GitHub': 'https://github.com/vidyasagar2110',
            'Twitter': 'https://twitter.com/yourusername'
        }
    }

    return render(request, 'index.html', context)
