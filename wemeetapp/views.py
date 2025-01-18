from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import os
import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import google.generativeai as genai


genai.configure(api_key='AIzaSyAfrDvCd8k5z14rH6qZYGUvJchxuJc6Lco')

    
# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email=request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username,email=email,password=password)
        if user is not None:
            return redirect('/') 

def signin(request):
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home/')  # Redirect to your home page after successful login
        
def message_page(request):
            return render(request,'messages.html')        


def chatbot(request):
     return render(request,'chatbot.html')


def return_home(request):
     return render(request,"home.html")

# def chatapi(request):
#      generation_config = {
#           "temperature": 1,
#           "top_p": 0.95,
#           "top_k": 64,
#           "max_output_tokens": 8192,
#           "response_mime_type": "text/plain",
#      }

#      model = genai.GenerativeModel(
#      model_name="gemini-2.0-flash-thinking-exp-1219",
#      generation_config=generation_config,
#      )

#      chat_session = model.start_chat(
#       history=[
#      ]
#      )

#      response = chat_session.send_message("INSERT_INPUT_HERE")

#      print(response.text)


def vcall(request):
     return render(request,'dashbord.html')

def videocall(request):
     return render(request,'videocall.html',{'name':request.user.username})


def join_room(request):
     if request.method=='POST':
          roomID=request.POST['roomID']
          return redirect("/meeting?roomID=" + roomID)
     return render(request,'joinroom.html')




# Model configuration
generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Initialize conversation history
history = []

# @csrf_exempt
# def chatbot_view(request):
#     global history
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             user_input = data.get('message', '')

#             chat_session = model.start_chat(history=history)
#             response = chat_session.send_message(user_input)
#             model_response = response.text

#             history.append({"role": "user", "parts": [user_input]})
#             history.append({"role": "model", "parts": [model_response]})

#             return JsonResponse({'response': model_response})
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#     elif request.method == 'GET':
#         return JsonResponse({'message': 'Chatbot endpoint is working. Send a POST request to interact.'})
#     return JsonResponse({'error': 'Invalid request method'}, status=400)





@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        try:
            # Ensure session exists
            if 'history' not in request.session:
                request.session['history'] = []

            # Parse user input
            data = json.loads(request.body)
            user_input = data.get('message', '')

            # Use session-stored history
            chat_session = model.start_chat(history=request.session['history'])
            response = chat_session.send_message(user_input)
            model_response = response.text

            # Update session history
            request.session['history'].append({"role": "user", "parts": [user_input]})
            request.session['history'].append({"role": "model", "parts": [model_response]})
            request.session.modified = True  # Mark the session as changed

            return JsonResponse({'response': model_response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    elif request.method == 'GET':
        return JsonResponse({'message': 'Chatbot endpoint is working. Send a POST request to interact.'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def chatbot_page(request):
    return render(request, 'chatbot.html')