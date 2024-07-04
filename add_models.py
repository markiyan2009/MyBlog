from MyBlog.blog.models import Post
import datetime




post = Post(title = "Футбол", content = "dsfoamsdomoamfomwoemgoasmogmadsmgoewmomaosdmgoasdmogmeomgoamsodmgoamdsgmamdsogmaodsmgoadmgmsdogmodsamglamsdlgmaldsmglamdsglamdslgmasldgmlasdmglasmdglamdlgmadlg", published_date = datetime.datetime(2024,5,15,12,0,0))
post.save()