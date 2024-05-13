import os
import django
from django.db.models import Q, Case, When, Value, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop


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
    ArtworkGallery.objects.filter(rating__lt=0).delete()


# delete_negative_rated_arts()

# print(ArtworkGallery.objects.all())


# Task2
def show_the_most_expensive_laptop() -> str:
    expensive_laptop = Laptop.objects.all().order_by('-price', 'id').first()

    return f"{expensive_laptop.brand} is the most expensive laptop available for {expensive_laptop.price}$!"


# print(show_the_most_expensive_laptop())


def bulk_create_laptops(*args):
    new_laptops = []

    for laptop in args:
        new_laptops.append(laptop)

    Laptop.objects.bulk_create(*new_laptops)


# Create a list of instances
# laptops_to_create = [laptop1, laptop2, laptop3]
# bulk_create_laptops(laptops_to_create)
def update_to_512_GB_storage() -> None:
    # all_laptops = Laptop.objects.all()
    #
    # for laptop in all_laptops:
    #     if laptop.brand in ["Asus", "Lenovo"]:
    #         laptop.storage = 512
    #         laptop.save()

    Laptop.objects.filter(Q(brand="Lenovo") | Q(brand="Asus")).update(storage=512)
    # Laptop.objects.filter(brand__in=["Lenovo","Asus"]).update(storage=512)


# update_to_512_GB_storage()


def update_to_16_GB_memory() -> None:
    # all_laptops = Laptop.objects.all()
    #
    # for laptop in all_laptops:
    #     if laptop.brand in ["Apple", "Dell", "Acer"]:
    #         laptop.memory = 16
    #         laptop.save()

    Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).update(memory=16)


update_to_16_GB_memory()


def update_operation_systems() -> None:
    # all_laptops = Laptop.objects.all()
    #
    # for laptop in all_laptops:
    #     if laptop.brand in ["Dell", "Acer"]:
    #         laptop.operation_system = "Linux"
    #         laptop.save()
    #
    # Laptop.objects.filter(brand="Asus").update(
    #     operation_system='Windows'
    # )
    #
    # Laptop.objects.filter(brand="Apple").update(
    #     operation_system='MacOS'
    # )
    #
    # Laptop.objects.filter(brand="Lenovo").update(
    #     operation_system='Chrome OS'
    # )

    Laptop.objects.update(
        operation_system=Case(
            When(brand="Asus", then=Value("Windows")),
            When(brand__in=["Dell", "Acer"], then=Value("Linux")),
            When(brand="Apple", then=Value("MacOS")),
            When(brand="Lenovo", then=Value("Chrome OS")),
            default=F('operation_system')
        )
    )


# update_operation_systems()


def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()


# delete_inexpensive_laptops()

laptop1 = Laptop(
    brand='Asus',
    processor='Intel Core i5',
    memory=8,
    storage=256,
    operation_system='Windows',
    price=899.99
)

laptop2 = Laptop(
    brand='Apple',
    processor='Apple M1',
    memory=16,
    storage=512,
    operation_system='MacOS',
    price=1399.99

)

laptop3 = Laptop(
    brand='Lenovo',
    processor='AMD Ryzen 7',
    memory=12,
    storage=512,
    operation_system='Linux',
    price=999.99,
)

# # Create a list of instances
# laptops_to_create = [laptop1, laptop2, laptop3]
#
# # Use bulk_create to save the instances
# bulk_create_laptops(laptops_to_create)
#
# # Execute the following functions
# update_to_512_GB_storage()
# update_operation_systems()
#
# # Retrieve 2 laptops from the database
# asus_laptop = Laptop.objects.filter(brand__exact='Asus').get()
# lenovo_laptop = Laptop.objects.filter(brand__exact='Lenovo').get()
#
# print(asus_laptop.storage)
# print(lenovo_laptop.operation_system)
