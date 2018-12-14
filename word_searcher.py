class Solution(object):
    def findWords(self, board, words):
        match_words={}
        for word in words:
            reversed_word = list(reversed(word))
            if (self.isWordPresentInBoard(board,word,0,0,0)) or (self.isWordPresentInBoard(board,reversed_word,0,0,0)):
               match_words[word]=word
        
        return sorted(match_words)
    
    def isWordPresentInBoard(self,board,word,word_character_index,current_row,current_col):
        word_len = len(word)
        board_rows_len = len(board)
        board_cols_len = len(board[0])

        if word_character_index < word_len:
           if (current_row < board_rows_len) and (current_col < board_cols_len):
              if word[word_character_index] == board[current_row][current_col]:
                 return (self.isWordPresentInBoard(board, word, (word_character_index + 1), (current_row + 1), current_col)) \
                     or (self.isWordPresentInBoard(board, word, (word_character_index + 1), current_row, (current_col + 1)))
              else:
                 if word_character_index == 0:
                    return (self.isWordPresentInBoard(board, word, word_character_index, (current_row + 1), current_col)) \
                    or (self.isWordPresentInBoard(board, word, word_character_index, current_row, (current_col + 1)))
                 else:
                    return False
           else:
               return False
        else:
            return True
