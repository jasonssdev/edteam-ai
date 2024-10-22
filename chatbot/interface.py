import gradio as gr

def greet(name, part_of_the_day, tempeture_f):
    part_of_the_day_dict = {'morning':'Goog morning', 'afternoon': 'Good afternoon', 'night': 'Good night'}
    temperature = round((tempeture_f - 32) * 5/9, 2)
    if part_of_the_day in part_of_the_day_dict:
        return f'{part_of_the_day_dict[part_of_the_day]} {name}, current temperature is {temperature} celsius degrees'

app = gr.Interface(
    fn=greet,
    inputs=["text", "text", gr.Slider(0,100)],
    outputs='text'
    )

app.launch()