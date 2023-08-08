from config import llm
from langchain.prompts import PromptTemplate
import json

class ProductSpecificationGenerator:
        
    def get_keywords(self, productname):
        prompt = f"""
        generate specifications for {productname} in list form and list should only contains the specification name not the description of specification
        """
        response=llm.predict(prompt)
        return response
    
    def get_specifications(self, productskeywords, productname, description):
        prompt = f"""
        generate specifications of the {productname} according to a list of keywords : {productskeywords} \n
        and fill the keywords with value using product description: {description}
        return the response in the form of dictionary format
        """
        
        response = llm.predict(prompt)
        return response
    

class InputHnadler:
    
    def get_product_name(inputdata):
        inputdata = input("enter product name: ")
        return inputdata
    
    def get_description(description):
        description = input("eneter product description:\n")
        return description 
    



if __name__ == "__main__":
    
    inputobj = InputHnadler()
    productname = inputobj.get_product_name()
    
    productobj = ProductSpecificationGenerator()
    productskeywords = productobj.get_keywords(productname)
    
    print(productskeywords)
        
    productdescription = inputobj.get_description()
    print(productdescription)
    
    productspecifications = productobj.get_specifications(productskeywords,productname,productdescription)
    print(productspecifications)
    
    
    # parse the output to dictionary format
    cleaned_response = productspecifications.strip().replace('\"', '').replace('    ','').split('\n')
    specs_dict = {}
    
    for line in cleaned_response:
        parts = line.split(': ')
        if len(parts) == 2:
            specs_dict[parts[0]] = parts[1]
            
    # exporting data to json file
    output_filename = f"{productname}_specifications.json"
    with open(output_filename, 'w') as json_file:
        json.dump(specs_dict, json_file, indent=4)

    print(f"Specifications saved to {output_filename}")
    
    
    
    
    