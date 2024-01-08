import modelbit, sys
import cloudpickle
from typing import *


with open('pipe-int4.pkl', 'rb') as file:
    pipe = cloudpickle.load(file)
    
# main function
def mistral_prompt(prompt):
    sequences = pipe(
        prompt,
        do_sample=False,
        max_new_tokens=300,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        num_return_sequences=1,
    )
    return {'output': sequences[0]['generated_text']}

# to run locally via git & terminal, uncomment the following lines
# if __name__ == "__main__":
#   print(mistral_prompt(*(modelbit.parseArg(v) for v in sys.argv[1:])))