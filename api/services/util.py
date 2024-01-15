def create_exhibition_dict (title, description, start_date, end_date, url, image_url=""):
     return {
        "title": title,
        "description": description,
        "startDate": start_date,
        "endDate": end_date,
        "websiteUrl": url,
        "imageUrl": image_url
    }

