import os
from datasets import load_dataset

def prepare_wikitext():
    """WikiText-2 데이터셋 다운로드 및 준비"""
    print("📥 Downloading WikiText-2...")
    dataset = load_dataset("wikitext", "wikitext-2-raw-v1")
    
    output_dir = "./wikitext-2-prepared"
    dataset.save_to_disk(output_dir)
    
    print(f"✅ Dataset saved to {output_dir}")
    print(f"📊 Train samples: {len(dataset['train'])}")
    print(f"📊 Validation samples: {len(dataset['validation'])}")
    print(f"📊 Test samples: {len(dataset['test'])}")
    
    return output_dir

if __name__ == "__main__":
    # 데이터셋 준비
    wikitext_dir = prepare_wikitext()
    
    # 환경 변수에서 S3 정보 가져오기
    s3_bucket = os.environ.get('S3_BUCKET_NAME')
    aws_region = os.environ.get('AWS_REGION', 'us-east-1')
    
    if s3_bucket:
        s3_path = f"s3://{s3_bucket}/data/wikitext-2/"
        
        print(f"\n📤 To upload to S3, run the following command:")
        print(f"\naws s3 sync {wikitext_dir} {s3_path} --region {aws_region}")
    else:
        print("\n⚠️  S3_BUCKET_NAME environment variable not set.")
        print("Set it with: export S3_BUCKET_NAME=your-bucket-name")
        print(f"\nThen run:")
        print(f"aws s3 sync {wikitext_dir} s3://YOUR-BUCKET/data/wikitext-2/ --region us-east-1")