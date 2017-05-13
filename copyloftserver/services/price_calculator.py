from copyloftserver.models.models import Cover
from copyloftserver.models.models import CoverBinding
from copyloftserver.models.models import Page
from copyloftserver.models.models import PageQuality
from copyloftserver.models.models import InkType
from django.forms.models import model_to_dict


class PriceCalculator:
    def __init__(self,book_dict):
        self.cover = book_dict['cover_id']
        self.binding = book_dict['binding']
        self.page_count = book_dict['page_count']
        self.page_size = book_dict['page_size']
        self.page_quality = book_dict['page_quality']
        self.ink_type = book_dict['ink_type']
        self.book_dict = book_dict

    def cover_price(self):
        try:
            return self.cover.cost
        except AttributeError:
            return 0

    def binding_price(self):
        try:
            return self.binding.cost
        except AttributeError:
            return 0

    def page_size_price(self):
        try:
            return self.page_size.cost
        except AttributeError:
            return 0

    def page_quality_price(self):
        try:
            return self.page_quality.cost
        except AttributeError:
            return 0

    def ink_price(self):
        try:
            return self.ink_type.cost
        except AttributeError:
            return 0

    def get_cover(self):
        try:
            return model_to_dict(self.cover)
        except AttributeError:
            return None

    def get_binding(self):
        try:
            return model_to_dict(self.binding)
        except AttributeError:
            return None

    def get_page_size(self):
        try:
            return model_to_dict(self.page_size)
        except AttributeError:
            return None

    def get_page_quality(self):
        try:
            return model_to_dict(self.page_quality)
        except AttributeError:
            return None

    def get_ink(self):
        try:
            return model_to_dict(self.ink_type)
        except AttributeError:
            return None

    def get_total_price(self):
        cover_price = self.cover_price()
        binding_price = self.binding_price()
        page_size_price = self.page_size_price()
        page_quality_price = self.page_quality_price()
        ink_price = self.ink_price()

        page_count = self.page_count

        single_page_cost = page_size_price + page_quality_price +ink_price
        total_page_cost = single_page_cost * page_count
        total_cost = cover_price + binding_price + total_page_cost

        return total_cost

    def get_reason(self):
        cover_price = self.cover_price()
        binding_price = self.binding_price()
        page_size_price = self.page_size_price()
        page_quality_price = self.page_quality_price()
        ink_price = self.ink_price()

        page_count = self.page_count

        single_page_cost = page_size_price + page_quality_price +ink_price
        total_page_cost = single_page_cost * page_count
        total_cost = cover_price + binding_price + total_page_cost

        return {'cover_price' : cover_price,
                'binding_price' : binding_price,
                'page_size_price' : page_size_price,
                'page_quality_price' : page_quality_price,
                'ink_price' : ink_price,
                'page_count' : page_count,
                'single_page_cost' : single_page_cost,
                'total_page_cost' : total_page_cost,
                'total_cost' : total_cost
                }