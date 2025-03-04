import requests
import json
import gradio as gr


url="http://localhost:11434/api/generate"


headers={
    'Content-Type': 'application/json',
}

#to sustain the memory
history=[]

def generate_response(prompt):
    #append the prompt in history 
    history.append(prompt)
    
    #collection of all the prompts
    final_prompt="\n".join(history)
    
    data={
        "model":"llama2",
        "prompt":final_prompt,
        "stream": False
    }
    
    #make a request and get response
    response=requests.post(url,headers=headers,data=json.dumps(data))
    print(response)
    
    if response.status_code==200:
        #collecting text from response
        response=response.text
        #load the response in json 
        data=json.loads(response)
        actual_response=data["response"]
        return actual_response
    else:
        print("Error:",response.text)
        
#creating ui
interface=gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=2,placeholder="Enter your prompt"),
    outputs="text"
)
interface.launch()
    

