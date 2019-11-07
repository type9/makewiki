from django.shortcuts import render, loader
from wiki.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class PageList(ListView):
    """
    CHALLENGES:
      1. On GET, display a homepage that shows all Pages in your wiki.
      2. Replace this CHALLENGE text with a descriptive docstring for PageList.
      3. Replace pass below with the code to render a template named `list.html`.
    """
    """
      This class extends ListView to render an index of pages using Page objects
    """
    model = Page

    def get(self, request):
        """ Returns a list of wiki pages. """
        page_list = Page.objects.all()
        context = {
          'page_list': page_list,
        }
        return render(request, 'list.html', context)


class PageDetailView(DetailView):
    """
    CHALLENGES:
      1. On GET, render a template named `page.html`.
      2. Replace this docstring with a description of what thos accomplishes.

    STRETCH CHALLENGES:
      1. Import the PageForm class from forms.py.
          - This ModelForm enables editing of an existing Page object in the database.
      2. On GET, render an edit form below the page details.
      3. On POST, check if the data in the form is valid.
        - If True, save the data, and redirect back to the DetailsView.
        - If False, display all the errors in the template, above the form fields.
      4. Instead of hard-coding the path to redirect to, use the `reverse` function to return the path.
      5. After successfully editing a Page, use Django Messages to "flash" the user a success message
           - Message Content: REPLACE_WITH_PAGE_TITLE has been successfully updated.
    """
    """
    This view renders a detailed view of the article based off of url slug
    """
    model = Page

    def get(self, request, slug):
        """ Returns a specific of wiki page by slug. """
        page_object = Page.objects.get(slug=slug)
        context = {
          'page': page_object,
        }
        return render(request, 'page.html', context)

    def post(self, request, slug):
        pass
