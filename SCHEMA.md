# Untitled

# Schema Structure:

**WORD_STREAM** (stream_id, word@, timestamp, minute@)

**MINUTE_SUMMARY** (minute@, total_word_count, vocab_size)

**WORD_TRENDINESS** (word@, minute@, word_count, trendiness)

# Brief Explanation:

**WORD_STREAM:** Store the raw information of tweets taking **words** as atomic units.

**MINUTE_SUMMARY:** Summary of vocabulary statistics for each **minute.**

**WORD_TRENDINESS:** Record the occurrence behaviors of **words** in each **minutes**.