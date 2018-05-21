//
//  ViewController.m
//  TESTURL
//
//  Created by Martin Chibwe on 5/18/18.
//  Copyright © 2018 Martin Chibwe. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    
    NSURL *urlString =  [NSURL URLWithString:@"https://api.edamam.com/search?q=apple&app_id=b088da30&app_key=4d45a9963d006ce6d48275df6482643b"];
    NSURL *url = [NSURL URLWithString:urlString];
    NSMutableURLRequest * urlRequest = [NSMutableURLRequest requestWithURL:url];
//    NSData *requestData = [prams dataUsingEncoding:NSUTF8StringEncoding];
    
    [urlRequest setHTTPMethod:@"GET"];
    [urlRequest setValue:@"application/json" forHTTPHeaderField:@"Accept"];
    [urlRequest setValue:@"application/json" forHTTPHeaderField:@"Content-Type"];
    
    NSURLSessionDataTask * dataTask = [[NSURLSession sharedSession] dataTaskWithRequest:urlRequest completionHandler:^(NSData * _Nullable data, NSURLResponse * _Nullable response, NSError * _Nullable error) {
        NSLog(@"data=%@",data);
        
        if (data.length>0 && error==nil) {
            NSDictionary *dict = [NSJSONSerialization JSONObjectWithData:data options:0 error:NULL];
            NSLog(@"Dict=%@",dict);
            
            
        }
    }];
    [dataTask resume];
}


- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


@end
