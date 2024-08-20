from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User, Group
from .models import Customer

@receiver(post_save, sender=User)
def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
        )
        print('Profile created!')

        '''Customer.objects.create(user=instance)
        print('profile created!')'''

#post_save.connect(customer_profile, sender=User)

'''@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('profile updated!')
        
        try:
            instance.profile.save()
            print('profile updated!')
        except:
            Profile.objects.create(user=instance)
            print('profile created for existing user!')

#post_save.connect(create_profile, sender=User)'''
