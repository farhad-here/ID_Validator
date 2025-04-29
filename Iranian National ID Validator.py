import streamlit as st


#OOP for checking ID
class CheckId:
       def __init__(self,vorodi):
              self.vorodi = vorodi
       def checkValue(self):

              # the length of numbers must be 10
              # all the numbers must be between 0 and 9
              # all the numbers should be digit
              if len(self.vorodi) != 10 or not self.vorodi.isdigit():
                     # NOT VALID
                     return 'Not Valid'
                       


                  
              else:
                     c = [int(i) for i in str(self.vorodi)]
              
              # all the numbers should not be the same
                     if len(set(c)) == 1:
                            # NOT VALID
                            return 'Not Valid'
                            
                     else:
                     
                            # formula => ((10×digit1 + 9×digit2 + ... + 2×digit9) % 11 ) 
                            # if the result < 2 then result must be equal to 10th digit 
                            # elif result >= 2 then 10th digit must be equal to 11 - result
                         
                            ck = sum([j * c[i] for i,j in enumerate(range(10,1,-1))]) % 11
                            if (ck < 2 and c[-1] == ck) or (ck >= 2 and c[-1] == 11 - ck):
                                   #VALID
                                   return 'Valid'
                         
                            else:
                                   #NOT VALID
                                   return 'Not Valid'

    

#INPUT for ID_CARD
inpt = st.chat_input('please type the ID')
if inpt:
       ckId = CheckId(str(inpt))

       if ckId.checkValue() == 'Valid':
              st.success(f"{str(inpt)} is ✅ Valid")
       else:
              st.error(f"{str(inpt)} is❌ Not Valid")