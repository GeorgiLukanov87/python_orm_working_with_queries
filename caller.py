import os
import django
from django.db.models import Q, Case, When, Value, F, IntegerField

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon, Workout


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


# update_to_16_GB_memory()


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

# Task 3
def bulk_create_chess_players(*args: ChessPlayer) -> None:
    ChessPlayer.objects.bulk_create(*args)


# Create two instances of ChessPlayer
player1 = ChessPlayer(
    username='Player1',
    title='no title',
    rating=2200,
    games_played=50,
    games_won=20,
    games_lost=25,
    games_drawn=5,
)

player2 = ChessPlayer(
    username='Player2',
    title='IM',
    rating=2350,
    games_played=80,
    games_won=40,
    games_lost=25,
    games_drawn=15,
)


# # Call the bulk_create_chess_players function
# bulk_create_chess_players([player1, player2])


def delete_chess_players() -> None:
    ChessPlayer.objects.filter(title='no title').delete()


# delete_chess_players()

def change_chess_games_won() -> None:
    ChessPlayer.objects.filter(title='GM').update(games_won=30)


# change_chess_games_won()


def change_chess_games_lost() -> None:
    ChessPlayer.objects.filter(title='no title').update(games_lost=25)


# change_chess_games_lost()


def change_chess_games_drawn() -> None:
    ChessPlayer.objects.all().update(games_drawn=10)


# change_chess_games_drawn()


def grand_chess_title_GM() -> None:
    ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')


# grand_chess_title_GM()


def grand_chess_title_IM() -> None:
    ChessPlayer.objects.filter(rating__range=(2300, 2399)).update(title="IM")


# grand_chess_title_IM()

def grand_chess_title_FM() -> None:
    ChessPlayer.objects.filter(rating__range=(2200, 2299)).update(title="IM")


# grand_chess_title_FM()


def grand_chess_title_regular_player() -> None:
    ChessPlayer.objects.filter(rating__range=(0, 2199)).update(title="regular player")


# grand_chess_title_regular_player()


# Task 4
def set_new_chefs() -> None:
    Meal.objects.update(
        chef=Case(
            When(meal_type='Breakfast', then=Value('Gordon Ramsay')),
            When(meal_type='Lunch', then=Value('Julia Child')),
            When(meal_type='Dinner', then=Value('Jamie Oliver')),
            When(meal_type='Snack', then=Value('Thomas Keller')),
            default=F('meal_type'),
        )
    )


# Meal.objects.create(
#     name="Pancakes",
#     meal_type="Breakfast",
#     preparation_time="20 minutes",
#     difficulty=3,
#     calories=350,
#     chef="Jane",
# )
#
# Meal.objects.create(
#     name="Spaghetti Bolognese",
#     meal_type="Dinner",
#     preparation_time="45 minutes",
#     difficulty=4,
#     calories=550,
#     chef="Sarah",
# )


# set_new_chefs()


def set_new_preparation_times() -> None:
    Meal.objects.update(
        preparation_time=Case(
            When(meal_type='Breakfast', then=Value('10 minutes')),
            When(meal_type='Lunch', then=Value('12 minutes')),
            When(meal_type='Dinner', then=Value('15 minutes')),
            When(meal_type='Snack', then=Value('5 minutes')),
            default=F('meal_type'),
        )
    )


# set_new_preparation_times()


def update_low_calorie_meals() -> None:
    Meal.objects.filter(meal_type__in=['Breakfast', 'Dinner']).update(calories=400)


# update_low_calorie_meals()


def update_high_calorie_meals() -> None:
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).update(calories=700)


# update_high_calorie_meals()


def delete_lunch_and_snack_meals() -> None:
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).delete()


# delete_lunch_and_snack_meals()


# Create two instances of the Meal model
# meal1 = Meal.objects.create(
#     name="Pancakes",
#     meal_type="Breakfast",
#     preparation_time="20 minutes",
#     difficulty=3,
#     calories=350,
#     chef="Jane",
# )
#
# meal2 = Meal.objects.create(
#     name="Spaghetti Bolognese",
#     meal_type="Dinner",
#     preparation_time="45 minutes",
#     difficulty=4,
#     calories=550,
#     chef="Sarah",
# )


# # Test the set_new_chefs function
# set_new_chefs()
#
# # Test the set_new_preparation_times function
# set_new_preparation_times()
#
# # Refreshes the instances
# meal1.refresh_from_db()
# meal2.refresh_from_db()
#
# # Print the updated meal information
# print("Meal 1 Chef:", meal1.chef)
# print("Meal 1 Preparation Time:", meal1.preparation_time)
# print("Meal 2 Chef:", meal2.chef)
# print("Meal 2 Preparation Time:", meal2.preparation_time)


# Task 5
def show_hard_dungeons() -> str:
    hard_dungeons = Dungeon.objects.filter(difficulty='Hard').order_by('location')

    return f'\n'.join(str(d) for d in hard_dungeons)


dungeon3 = Dungeon(
    name="Dungeon 3",
    boss_name="Boss 3",
    boss_health=2000,
    recommended_level=175,
    reward="Gold",
    location="Eternal Hell 2",
    difficulty="Hard",
)

dungeon4 = Dungeon(
    name="Dungeon 4",
    boss_name="Boss 4",
    boss_health=1500,
    recommended_level=125,
    reward="Experience",
    location="Crystal Caverns",
    difficulty="Easy",
)


# print(show_hard_dungeons())


def bulk_create_dungeons(*args: Dungeon) -> None:
    Dungeon.objects.bulk_create(*args)


# bulk_create_dungeons([dungeon3, dungeon4])


def update_dungeon_names() -> None:
    Dungeon.objects.update(
        name=Case(
            When(difficulty='Easy', then=Value('The Erased Thombs')),
            When(difficulty='Medium', then=Value('The Coral Labyrinth')),
            When(difficulty='Hard', then=Value('The Lost Haunt')),
            default=F('difficulty'),
        )
    )


# update_dungeon_names()


def update_dungeon_bosses_health() -> None:
    Dungeon.objects.exclude(difficulty__in=['Easy']).update(boss_health=500)


update_dungeon_bosses_health()


def update_dungeon_recommended_levels() -> None:
    # Dungeon.objects.filter(difficulty='Easy').update(
    #     recommended_level=25
    # )
    #
    # Dungeon.objects.filter(difficulty='Medium').update(
    #     recommended_level=50
    # )
    # Dungeon.objects.filter(difficulty='Hard').update(
    #     recommended_level=75
    # )

    Dungeon.objects.update(
        recommended_level=Case(
            When(difficulty="Easy", then=Value(25)),
            When(difficulty="Medium", then=Value(50)),
            When(difficulty="Hard", then=Value(75)),
            default=Value(0),  # Default value in case none of the conditions match
            output_field=IntegerField()
        )
    )


# update_dungeon_recommended_levels()


def update_dungeon_rewards() -> None:
    Dungeon.objects.filter(boss_health=500).update(reward='1000 Gold')
    Dungeon.objects.filter(location__startswith='E').update(reward='New dungeon unlocked')
    Dungeon.objects.filter(location__endswith='s').update(reward='Dragonheart Amulet')


# update_dungeon_rewards()


def set_new_locations() -> None:
    Dungeon.objects.update(
        location=Case(
            When(recommended_level=25, then=Value('Enchanted Maze')),
            When(recommended_level=50, then=Value('Brimstone Mines')),
            When(recommended_level=75, then=Value('Shadowed Abyss')),
        )
    )


# set_new_locations()


# Task 6
def show_workouts() -> str:
    filtered_workouts = Workout.objects.filter(workout_type__in=['Calisthenics', 'CrossFit'])

    return '\n'.join(str(wo) for wo in filtered_workouts)


# workout1 = Workout.objects.create(
#     name="Push-Ups",
#     workout_type="Calisthenics",
#     duration="10 minutes",
#     difficulty="Intermediate",
#     calories_burned=200,
#     instructor="Chris Heria"
# )
#
# workout2 = Workout.objects.create(
#     name="Running",
#     workout_type="Cardio",
#     duration="30 minutes",
#     difficulty="High",
#     calories_burned=400,
#     instructor="John Smith"
# )

# print(show_workouts())
def get_high_difficulty_cardio_workouts() -> Workout:
    return Workout.objects.filter(workout_type='Cardio').filter(difficulty='High').order_by('instructor')


# print(get_high_difficulty_cardio_workouts())


def set_new_instructors() -> None:
    Workout.objects.update(
        instructor=Case(
            When(workout_type='Cardio', then=Value('John Smith')),
            When(workout_type='Strength', then=Value('Michael Williams')),
            When(workout_type='Yoga', then=Value('Emily Johnson')),
            When(workout_type='CrossFit', then=Value('Sarah Davis')),
            When(workout_type='Calisthenics', then=Value('Chris Heria')),
            default=F('workout_type'),
        )
    )


# set_new_instructors()


def set_new_duration_times() -> None:
    Workout.objects.update(
        duration=Case(
            When(instructor='John Smith', then=Value('15 minutes')),
            When(instructor='John Smith', then=Value('15 minutes')),
            When(instructor='Sarah Davis', then=Value('30 minutes')),
            When(instructor='Chris Heria', then=Value('45 minutes')),
            When(instructor='Michael Williams', then=Value('1 hour')),
            When(instructor='Emily Johnson', then=Value('1 hour and 30 minutes')),
            default=F('instructor'),
        )
    )


# set_new_duration_times()

def delete_workouts() -> None:
    workouts_to_delete = Workout.objects.exclude(workout_type__in=['Strength', 'Calisthenics'])
    workouts_to_delete.delete()

# delete_workouts()
