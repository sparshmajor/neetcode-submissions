import math

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        # Final result containing all justified lines
        res = []

        def fill(_words, spaces_left):
            """
            Creates a fully justified line.

            Example:
                words = ["This", "is", "fun"]
                spaces_left = 8

            We distribute spaces as evenly as possible.
            If spaces cannot be divided equally,
            extra spaces are added to the LEFT gaps first.

            For example:
                "This____is___fun"

            where left gaps get more spaces.
            """

            _str = ""
            # Number of words remaining to process
            l = len(_words)

            for _w in _words:
                # Add current word
                _str += _w

                """
                Number of gaps remaining = l - 1

                Example:
                    ["a", "b", "c"]

                Initially:
                    l = 3
                    gaps = 2

                We use ceil() so that left side gaps
                get extra spaces first.
                """

                # If only one word exists in line,
                # all remaining spaces go after that word
                f = math.ceil(spaces_left / (l - 1)) if l - 1 != 0 else spaces_left

                # Add calculated spaces
                _str += " " * f

                # One word processed
                l -= 1

                # Remove used spaces from remaining pool
                spaces_left -= f

            # Store justified line
            res.append(_str)

        # Stores words of current line
        temp = []

        """
        temp_space:
            Minimum spaces required between words.
            If we have N words,
            minimum spaces needed = N - 1

            We increment this while building line
            to check whether line can fit.
        """
        temp_space = 0

        # Total characters count of words only
        count = 0

        for i, w in enumerate(words):

            # Add word to current line
            temp.append(w)

            # Add word length
            count += len(w)

            # One more space needed between words
            temp_space += 1

            """
            Current line length becomes:
                total_word_chars + minimum_required_spaces

            temp_space - 1 because:
                for N words,
                minimum gaps = N - 1
            """
            if count + temp_space - 1 > maxWidth:

                # Current word overflowed line
                # Remove it
                _t = temp.pop()

                """
                count currently includes overflow word length.
                Remove it before calculating spaces.

                spaces_left =
                    maxWidth - total_characters_of_valid_words
                """
                fill(temp, maxWidth - (count - len(_t)))

                # Start new line with overflow word
                temp = [_t]

                # Reset variables for new line
                temp_space = 1
                count = len(_t)

        """
        Last line handling:
            - Left justified
            - Only one space between words
            - Remaining spaces added at end

        Example:
            "last line____"
        """
        res.append(
            " ".join(temp) +
            (" " * (maxWidth - (count + (len(temp) - 1))))
        )

        return res