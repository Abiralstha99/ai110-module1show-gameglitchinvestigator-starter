import pytest
from logic_utils import check_guess, update_score


# --- existing tests (fixed: check_guess returns a tuple, not a bare string) ---

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Test 1 ---
# Catches Bug 1: the hint messages were swapped — "Too High" was returning
# "📈 Go HIGHER!" instead of "📉 Go LOWER!", sending the player the wrong way.
def test_check_guess_too_high_message_says_go_lower():
    outcome, message = check_guess(80, 50)  # 80 > 50, so guess is too high
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!", (
        f"Expected 'Go LOWER' hint for a high guess, got: {message!r}"
    )
    assert "HIGHER" not in message, "A too-high guess must NOT say Go HIGHER"


# --- Test 2 ---
# Catches Bug 2: on even attempts, the secret was cast to str before being
# passed to check_guess(). In Python 3, comparing int > str raises TypeError,
# which silently corrupts the hint or crashes the game.
def test_check_guess_correct_types():
    # With both values as int, 9 < 50 → Too Low, Go HIGHER
    outcome, message = check_guess(9, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_check_guess_string_secret_raises():
    # If the secret is accidentally a str (the type-cast bug), Python raises
    # TypeError instead of returning a valid hint — the game breaks silently.
    with pytest.raises(TypeError):
        check_guess(9, "50")


# --- Test 3 ---
# Catches the general contract of update_score: wins add points, wrong guesses
# deduct 5. If either branch is broken, scoring silently misbehaves.
def test_update_score_wrong_guess_deducts_five():
    # Each wrong guess (Too High or Too Low) should cost exactly 5 points.
    assert update_score(100, "Too High", 1) == 95
    assert update_score(100, "Too Low", 1) == 95


def test_update_score_win_adds_points():
    # A correct guess should increase the score, not leave it unchanged.
    score_after = update_score(0, "Win", 1)
    assert score_after > 0, "Winning should award points"


# --- Test 4 ---
# Catches Bug 6 (off-by-one): attempts was initialised to 1 instead of 0,
# so the first win used attempt_number=2 → 100 - 10*(2+1) = 70 instead of
# the correct 100 - 10*(1+1) = 80.
def test_update_score_win_bonus_first_attempt():
    score = update_score(0, "Win", 1)
    assert score == 80, (
        f"Expected 80 points for winning on attempt 1, got {score}. "
        "Likely caused by attempts initialised to 1 instead of 0."
    )
