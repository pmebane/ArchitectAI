def format_stream_response(report,event):
    report.append(event['choices'][0]['delta']['content'])
    result= "".join(report).strip()
    result = result.replace("\*","")
    return result