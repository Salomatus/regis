from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Удаляет всё, затем добавляет тестовые продукты"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(self.style.WARNING("Все продукты и категории были удалены."))

        watch = Category.objects.create(name="Аксессуары", description="Часы")
        shoes = Category.objects.create(name="Сапоги", description="Обувь")

        self.stdout.write(
            self.style.SUCCESS(f"Созданы категории: {watch.name}, {shoes.name}")
        )

        Product.objects.create(
            name="Happy Sport",
            description="Ювелирные женские",
            price=1274000,
            category=watch,
        )
        Product.objects.create(
            name="Zenith",
            description="Не ювелирные мужские",
            price=910000,
            category=watch,
        )
        Product.objects.create(
            name="LeSilla", description="Ботфорты", price=99500, category=shoes
        )

        self.stdout.write(self.style.SUCCESS("Добавлены тестовые продукты."))
