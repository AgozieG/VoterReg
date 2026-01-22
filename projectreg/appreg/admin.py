from django.contrib import admin
from .models import Voter, Farmer, Vote

@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    list_display = ('id','surname','firstname','phone','rc_number','mine_name','created_at')
    list_filter = ('rc_number','marital_status','gender','created_at')
    search_fields = ('surname','firstname','email','phone','mine_name','rc_number')
    readonly_fields = ('created_at','unique_voter_number')
    ordering = ('-created_at',)


@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('id','name','votes_count','created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at','votes_count')
    ordering = ('-votes_count',)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('id','voter','farmer','created_at')
    search_fields = ('voter__firstname','voter__surname','farmer__name')
    ordering = ('-created_at',)
