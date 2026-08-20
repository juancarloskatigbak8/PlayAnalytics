from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import PlayerProfile, PlayerNotes
from .forms import PlayerNoteForm, PlayerProfileForm

# === Index/Landing Page View ===
@login_required
def index(request):
    return render(request, 'index.html')


# === Add a New Player ===
@login_required
def add_player(request):
    if request.method == 'POST':
        form = PlayerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('player_profiles:profile_list')
    else:
        form = PlayerProfileForm()
    
    return render(request, 'player_profiles/add_player.html', {'form': form})


# === Edit an Existing Player's Profile ===
@login_required
def edit_player(request, player_id):
    player = get_object_or_404(PlayerProfile, pk=player_id)

    if request.method == 'POST':
        form = PlayerProfileForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_profiles:profile_detail', pk=player.id)
    else:
        form = PlayerProfileForm(instance=player)

    return render(request, 'player_profiles/edit_player.html', {
        'form': form,
        'player': player
    })


# === List All Player Profiles ===
@login_required
def profile_list(request):
    profiles = PlayerProfile.objects.all()
    return render(request, 'player_profiles/profile_list.html', {
        'profiles': profiles
    })


# === View Player Profile Detail + Add Note ===
@login_required
def profile_detail(request, pk):
    profile = get_object_or_404(PlayerProfile, pk=pk)
    notes = profile.notes.all().order_by('-created_at')

    if request.method == 'POST':
        note_form = PlayerNoteForm(request.POST)
        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.player = profile
            note.save()
            return redirect('player_profiles:profile_detail', pk=pk)
    else:
        note_form = PlayerNoteForm()

    return render(request, 'player_profiles/profile_detail.html', {
        'profile': profile,
        'notes': notes,
        'note_form': note_form
    })


# === Delete Player Profile ===
@login_required
def delete_player(request, pk):
    player = get_object_or_404(PlayerProfile, pk=pk)
    if request.method == 'POST':
        player.delete()
        return redirect('player_profiles:profile_list')


# === Add Note to a Player ===
@login_required
def add_note(request, profile_id):
    profile = get_object_or_404(PlayerProfile, id=profile_id)

    if request.method == 'POST':
        form = PlayerNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.player = profile
            note.save()
            return redirect('player_profiles:profile_detail', pk=profile.id)
    else:
        form = PlayerNoteForm()

    return render(request, 'player_profiles/add_note.html', {
        'form': form,
        'profile': profile
    })


# === Delete a Player's Note ===
@login_required
def delete_note(request, note_id):
    note = get_object_or_404(PlayerNotes, pk=note_id)
    profile_id = note.player.id
    note.delete()
    return redirect('player_profiles:profile_detail', pk=profile_id)


# === Edit an Existing Note ===
@login_required
def edit_note(request, note_id):
    note = get_object_or_404(PlayerNotes, id=note_id)

    if request.method == 'POST':
        form = PlayerNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('player_profiles:profile_detail', pk=note.player.id)
    else:
        form = PlayerNoteForm(instance=note)

    return render(request, 'player_profiles/edit_note.html', {
        'form': form,
        'note': note
    })
