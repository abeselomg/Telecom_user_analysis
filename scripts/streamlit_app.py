import streamlit as st
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

def app():

    st.title("User Analytics in the Telecommunication Industry")

    st.header("Data Analysis")
    # processed_tweets = pd.read_csv("../../data/economic_clean.csv")
    parent_dir =os.path.join( os.path.abspath(os.path.join(os.getcwd(), os.pardir)),"week 1")
    file_path=os.path.join(parent_dir, "data", "experience-analytics.csv")
    clean_csv = pd.read_csv(file_path)
    userdata_info=pd.read_csv(os.path.join(parent_dir, "data", "clean_user_info.csv"))
    # model_ready_tweets.clean_text = model_ready_tweets.clean_text.astype(str)

    st.header("I.Handsets")
    st.subheader("1.The Top 10 Handset Types")
    
    st.bar_chart(clean_csv["Handset Type"].value_counts().nlargest(10))
    st.subheader("2.The Top 5 Handset Manufacturers")
    st.bar_chart(clean_csv["Handset Manufacturer"].value_counts().nlargest(5))
    
    st.line_chart(userdata_info[["Total UL/DL","Youtube UL/DL"]])
    st.line_chart(userdata_info[["Total UL/DL", "Gaming UL/DL"]])
    st.area_chart(userdata_info[["Total UL/DL", "Gaming UL/DL"]])
    
    
    hist_data = [userdata_info["Total UL/DL"],userdata_info["Gaming UL/DL"]]
    group_labels = ["Total UL/DL","Gaming UL/DL"]
    fig = ff.create_distplot(hist_data, group_labels, bin_size=[10, 25])
    st.plotly_chart(fig, use_container_width=True)
    
    
    
    
    # st.subheader("2. Most Liked Tweets")
    # most_liked = processed_tweets[
    #     ["original_text", "original_author", "favorite_count"]
    # ].sort_values(by="favorite_count", ascending=False)[:5]
    # count = 1
    # for index in most_liked.index:
    #     st.text(
    #         "{}. {}'s Tweet\n\t{}\nwith {:,} likes".format(
    #             count,
    #             most_liked["original_author"][index],
    #             most_liked["original_text"][index],
    #             most_liked["favorite_count"][index],
    #         )
    #     )
    #     count += 1

    # st.subheader("3. Most Retweeted Tweets")
    # most_retweeted = processed_tweets[
    #     ["original_text", "original_author", "retweet_count"]
    # ].sort_values(by="retweet_count", ascending=False)[:5]
    # count = 1
    # for index in most_retweeted.index:
    #     st.text(
    #         "{}. {}'s Tweet\n\t{}\nwith {:,} retweets".format(
    #             count,
    #             most_retweeted["original_author"][index],
    #             most_retweeted["original_text"][index],
    #             most_retweeted["retweet_count"][index],
    #         )
    #     )
    #     count += 1
    # st.subheader("4. Users who Twitted Most")
    # st.bar_chart(processed_tweets.original_author.value_counts()[:5])

    # st.subheader("5. Users With Most Followers")
    # most_followers = processed_tweets[
    #     ["original_author", "followers_count"]
    # ].sort_values(by="followers_count", ascending=False)[:5]
    # count = 1
    # for index in most_followers.index:
    #     st.text(
    #         "{}. {} with {:,} followers".format(
    #             count,
    #             most_followers["original_author"][index],
    #             most_followers["followers_count"][index],
    #         )
    #     )
    #     count += 1

    # st.subheader("6. Users with Most Number of Friends")
    # most_friends = processed_tweets[["original_author", "friends_count"]].sort_values(
    #     by="friends_count", ascending=False
    # )[:5]
    # count = 1
    # for index in most_friends.index:
    #     st.text(
    #         "{}. {} with {:,} friends".format(
    #             count,
    #             most_friends["original_author"][index],
    #             most_friends["friends_count"][index],
    #         )
    #     )
    #     count += 1

    # st.subheader("7. Most used Hashtags")
    # hashtags = processed_tweets[["hashtags"]]
    # hashtags.dropna(inplace=True)
    # hashtags["hashtags"] = hashtags["hashtags"].astype(str)
    # hashtags["hashtags"] = hashtags["hashtags"].apply(lambda value: value.lower())
    # st.bar_chart(hashtags.hashtags.value_counts()[:5])

    # st.subheader("8. Most Mentioned")
    # st.bar_chart(processed_tweets.user_mentions.value_counts()[:5])

    # st.header("II. From Model Ready Tweets")
    # st.dataframe(model_ready_tweets)
    # st.subheader("Most used Words")
    # stopWords = set(stopwords.words("english"))
    # words_list = [
    #     word
    #     for words_list in model_ready_tweets.clean_text
    #     for word in words_list.split(" ")
    # ]

    # words_df = pd.DataFrame(
    #     [word for word in words_list if word not in stopWords and word != ""],
    #     columns=["words"],
    # )

    # st.bar_chart(words_df.words.value_counts()[:5])
    
    
app()
