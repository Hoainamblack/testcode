from ._anvil_designer import Form1Template
from anvil import *
import anvil.server 


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def image_1_show(self, **event_args):
    """This method is called when the Image is shown on the screen"""
    pass

  def button_sort_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass



class Form1(Form1Template):
    def __init__(self, **properties):
        # Khởi tạo form
        self.init_components(**properties)
        
        # Đăng ký sự kiện nhấn nút để thực hiện sắp xếp dãy số
        self.button_sort.set_event_handler('click', self.button_1_click)
    
    # Hàm xử lý sự kiện khi nhấn nút
    def button_1_click(self, **event_args):
        # Lấy dãy số từ Text Box
        input_text = self.text_box_1.text
        # Tách các số bằng khoảng trắng và chuyển thành list
        number_list = list(map(int, input_text.split()))
        
        # Sắp xếp dãy số
        sorted_numbers = sorted(number_list)
        
        # Hiển thị dãy số đã sắp xếp trong Label
        self.text_box_2.text = "Dãy số sau khi sắp xếp: " + " ".join(map(str, sorted_numbers))
