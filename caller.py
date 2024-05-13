import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery


# Task 1
def show_highest_rated_art() -> str:
    art = ArtworkGallery.objects.all().order_by('-rating').first()

    return f"{art.art_name} is the highest-rated art with a {art.rating} rating!"


# print(show_highest_rated_art())


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery) -> None:
    ArtworkGallery.objects.bulk_create([first_art, second_art])


# artwork1 = ArtworkGallery(artist_name="Vincent van Gogh", art_name="Starry Night", rating=4, price=1200000.0)
# artwork2 = ArtworkGallery(artist_name="Leonardo da Vinci", art_name="Mona Lisa", rating=5, price=1500000.0)

# Bulk saves the instances
# bulk_create_arts(artwork1, artwork2)


def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).update(rating=0)


# delete_negative_rated_arts()

# print(ArtworkGallery.objects.all())
