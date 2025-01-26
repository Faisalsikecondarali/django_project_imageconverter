from django.http import HttpResponse
from PIL import Image
import io

from django.http import HttpResponse
from PIL import Image, UnidentifiedImageError
import io

from django.http import HttpResponse
from PIL import Image, UnidentifiedImageError
import io

def convert_image(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('image')
        target_format = request.POST.get('format')

        if not uploaded_file:
            return HttpResponse('No image uploaded.', status=400)
        if not target_format:
            return HttpResponse('No target format specified.', status=400)

        try:
            # Open the uploaded image
            image = Image.open(uploaded_file)
            output = io.BytesIO()

            # Convert the image to the specified format
            image.save(output, format=target_format.upper())
            output.seek(0)

            # Return the converted image
            response = HttpResponse(output, content_type=f'image/{target_format}')
            response['Content-Disposition'] = f'attachment; filename=converted.{target_format}'
            return response
        except UnidentifiedImageError:
            return HttpResponse('Invalid image file.', status=400)
        except ValueError:
            return HttpResponse(f'Unsupported image format: {target_format}.', status=400)
        except Exception as e:
            return HttpResponse(f'Error: {str(e)}', status=500)
    else:
        return HttpResponse('Only POST requests are allowed.', status=405)


from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
